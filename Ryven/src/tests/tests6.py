"""An example financial data plotting application.

The application allows arbitrary number of plots (on the same axis).
For each plot, the x and y axis could represent any field of any stock.
Everything is reactive -- changes will automatically be reflected in the entire application.
"""

import edifice as ed
from edifice import Dropdown, IconButton, Label, ScrollView, Slider, TextInput, View
from edifice.components import plotting

import matplotlib.colors as mcolors
import pandas as pd
import yfinance as yf


def _create_state_for_plot(plotname):
    """Creates the state associated with a particular plot."""
    return {
        # Data to show on x-axis (data type, data source)
        f"{plotname}.xaxis.data": ("Date", "AAPL"),
        # Transformation applied to x-axis (transform type, transform param)
        f"{plotname}.xaxis.transform": ("None", 30),
        f"{plotname}.yaxis.data": ("Close", "AAPL"),
        f"{plotname}.yaxis.transform": ("None", 30),
        # Plot type (line or scatter) and plot color
        f"{plotname}.type": "line",
        f"{plotname}.color": "peru",
    }


def merge(d1, d2):
    """Helper function to merge two dictionaries."""
    d = d1.copy()
    d.update(d2)
    return d


# We store application state centrally. Each component can query this central store and
# set state, and all components that use that state will automatically update.
# See https://www.pyedifice.org/state.html
app_state = ed.StateManager(merge(_create_state_for_plot("plot0"), {
    "all_plots": ["plot0"],
    "next_i": 1,
}))


# We create a component which describes the options for each axis (data source, transform).
# Since this component owns no state, we can simply write a render function and use the
# make_component decorator.
@ed.make_component
def AxisDescriptor(self, name, key, children):
    # We subscribe to app_state, so that state changes would trigger a re-render
    # Subscribe returns the data stored in app_state
    data = app_state.subscribe(self, f"{key}.data")
    data_type, ticker = data.value
    transform = app_state.subscribe(self, f"{key}.transform")
    transform_type, param = transform.value
    # We can use CSS styling. See https://www.pyedifice.org/styling.html
    row_style = {"align": "left", "width": 350}
    return View(layout="column")(
        View(layout="row", style=row_style)(
            Label(name, style={"width": 40}),
            Dropdown(selection=data_type, options=["Date", "Close", "Volume"],
                     on_select=lambda text: data.set((text, ticker))),
            # if data_type != "Date", the following evaluates to False due to and short-circuiting.
            # A False or None child is treated as an empty slot
            data_type != "Date" and TextInput(
                text=ticker, style={"padding": 2},
                # The on_change callback is called whenever the change event fires,
                # i.e. when the input box text changes.
                on_change=lambda text: data.set((data_type, text))
            )
        ),
        View(layout="row", style=row_style)(
            Label("Transform:", style={"width": 70}),
            Dropdown(
                selection=transform_type, options=["None", "EMA"],
                on_select=lambda text: transform.set((text, param))
            ),
            transform == "EMA" and Label(f"Half Life ({param} days)", style={"width": 120}),
            transform == "EMA" and Slider(
                value=param, min_value=1, max_value=90, dtype=int,
                on_change=lambda val: transform.set((transform_type, val))
            )
        )
    )


# We create a shorthand for creating a component with a label
def labeled_elem(label, comp):
    return View(layout="row", style={"align": "left"})(
        Label(label, style={"width": 80}), comp,
    )


def add_divider(comp):
    return View(layout="column")(
        comp,
        View(style={"height": 0, "border": "1px solid gray"})
    )


# Now we make a component to describe the entire plot: the descriptions of both axis,
# plot type, and color
@ed.make_component
def PlotDescriptor(self, name, children):
    plot_type = app_state.subscribe(self, f"{name}.type")
    color = app_state.subscribe(self, f"{name}.color")
    return View(layout="row", style={"margin": 5})(
        View(layout="column", style={"align": "top"})(
            AxisDescriptor("x-axis", f"{name}.xaxis"),
            AxisDescriptor("y-axis", f"{name}.yaxis"),
        ),
        View(layout="column", style={"align": "top", "margin-left": 10})(
            labeled_elem(
                "Chart type",
                Dropdown(selection=plot_type.value, options=["scatter", "line"],
                         on_select=lambda text: plot_type.set(text))
            ),
            labeled_elem(
                "Color",
                Dropdown(selection=color.value, options=list(mcolors.CSS4_COLORS.keys()),
                         on_select=lambda text: color.set(text))
            )
        ),
    )


# Finally, we create a component that contains the plot descriptions, a button to add a plot,
# and the actual Matplotlib figure.
# To better organize the code, we create a class so that we can put plotting logic in methods.
class App(ed.Component):

    # Adding a plot is very simple conceptually (and in Edifice).
    # Just add new state for the new plot!
    def add_plot(self, e):
        next_key = "plot" + str(app_state["next_i"])
        app_state.update(merge(_create_state_for_plot(next_key), {
            "all_plots": app_state["all_plots"] + [next_key],
            "next_i": app_state["next_i"] + 1,
        }))

    # The Plotting function called by the plotting.Figure component.
    # The plotting function is passed a Matplotlib axis object.
    def plot(self, ax):
        all_plots = app_state["all_plots"]

        def get_state(df, label, transform, param):
            if label == "Date":
                return df.index
            if transform == "None":
                return df[label]
            return df[label].ewm(halflife=param).mean()

        for plot in all_plots:
            xdata, xticker = app_state.subscribe(self, f"{plot}.xaxis.data").value
            xtransform, xparam = app_state.subscribe(self, f"{plot}.xaxis.transform").value
            ydata, yticker = app_state.subscribe(self, f"{plot}.yaxis.data").value
            ytransform, yparam = app_state.subscribe(self, f"{plot}.yaxis.transform").value
            plot_type = app_state.subscribe(self, f"{plot}.type").value
            color = app_state.subscribe(self, f"{plot}.color").value

            xdf = yf.Ticker(xticker).history("1y")
            ydf = yf.Ticker(yticker).history("1y")

            df = pd.DataFrame({"xdata": get_state(xdf, xdata, xtransform, xparam)}, index=xdf.index)
            df = df.merge(pd.DataFrame({"ydata": get_state(ydf, ydata, ytransform, yparam)}, index=ydf.index),
                          left_index=True, right_index=True)
            if plot_type == "line":
                ax.plot(df.xdata, df.ydata, color=color)
            elif plot_type == "scatter":
                ax.scatter(df.xdata, df.ydata, color=color)

    def render(self):
        all_plots = app_state.subscribe(self, "all_plots").value
        return ed.MainWindow(title="Financial Charts")(
            View(layout="column", style={"margin": 10})(
                ScrollView(layout="column")(
                    *[add_divider(PlotDescriptor(plotname)) for plotname in all_plots]
                ),
                # Edifice comes with Font-Awesome icons for your convenience
                IconButton(name="plus", title="Add Plot", on_click=self.add_plot),
                # We create a lambda fuction so that the method doesn't compare equal to itself.
                # This forces re-renders everytime this entire component renders.
                plotting.Figure(lambda ax: self.plot(ax)),
            )
        )


# Finally to start the the app, we pass the Component to the edifice.App object
# and call the start function to start the event loop.
if __name__ == "__main__":
    ed.App(App(), inspector=True).start()
