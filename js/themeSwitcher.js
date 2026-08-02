// CURRENTLY UNUSED

// https://medium.com/swlh/dark-mode-using-css-variables-cf065a7fa133#:~:text=For%20example%2C%20--text-color%20in%20light%20mode%20can%20be,colors%20or%20shades%20of%20colors%20for%20new%20views.

const sun = document.querySelector("svg.sun");
const moon = document.querySelector("svg.moon");
const landingpage = document.querySelector(".landingpage");
const node_shadow_opacity = document.querySelectorAll("feFlood");
const li_imgs = document.querySelectorAll(".carousel-listitem img.invert");
const header = document.querySelector(".header.bg-dark");
const stylus_image = document.querySelector("#stylus_image");
const interface_image = document.querySelector(".interface");

// const theme_buttons = document.querySelectorAll(".theme-button");
// const theme_image = document.querySelector(".try-theme-image");
// const default_theme_dark = document.querySelector("#theme1");
// const default_theme_light = document.querySelector("#theme2");

const html = document.querySelector('html');
const isOsDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
// html.dataset.theme = `theme-${isOsDark ? 'dark' : 'light'}`;

if (isOsDark) {
  switchTheme('dark');
} else {
  switchTheme('light');
}

function switchTheme(theme) {
  if (theme === 'light') {

    // Change Icon
    sun.style.display = "block";
    moon.style.display = "none";

    // Custom Stuff
    header.setAttribute("style", "box-shadow: 0px 3px 35px #00000017");
    var z = node_shadow_opacity.length;
    while (z--) {
      node_shadow_opacity[z].setAttribute("flood-opacity", "0.07");
    }
    var i = li_imgs.length;
    while (i--) {
      li_imgs[i].setAttribute("style", "filter: invert(1)");
    }

    // Change selected theme
    // var i = theme_buttons.length;
    // while (i--) {
    // theme_buttons[i].classList.remove("active");
    // }
    // default_theme_light.classList.add("active");
    // theme_image.setAttribute("src", "img/themes/themes_1_samuel1l.png");


    // Change Images (new try for every page)
    try {
      landingpage.style.backgroundImage = "url('../static/img/BG-dots_light.png')";
      stylus_image.setAttribute("src", "../static/img/stylus_light.png");
      interface_image.setAttribute("src", "../static/img/screenshot_home_light.png");
    } catch (err) {console.log(err)}
    try {
      const docs_logo = document.querySelector(".docs-logo");
      docs_logo.setAttribute("src", "../static/img/docs/logo.png");
    } catch (err) {}


  } else {

    // Change Icon
    sun.style.display = "none";
    moon.style.display = "block";

    // Custom Stuff
    header.setAttribute("style", "box-shadow: 0px 3px 35px var(--shadow-color)");
    var z = node_shadow_opacity.length;
    while (z--) {
      node_shadow_opacity[z].setAttribute("flood-opacity", "0.231");
    }
    var i = li_imgs.length;
    while (i--) {
      li_imgs[i].setAttribute("style", "filter: invert(0)");
    }

    // Change selected theme

    // Change Images (new try for every page)
    try {
      landingpage.style.backgroundImage = "url('../static/img/BG-dots.png')";
      stylus_image.setAttribute("src", "../static/img/stylus_dark.png");
      interface_image.setAttribute("src", "../static/img/screenshot_home_dark.png");

    } catch (err) {}
    try {
      const docs_logo = document.querySelector(".docs-logo");
      docs_logo.setAttribute("src", "../static/img/docs/logo_white.png");
    } catch (err) {}

  }
  html.dataset.theme = `theme-${theme}`;
}