# for all *.ui files in ryven/gui/uic
for file in ryven/gui/uic/*.ui; do
    # get filename without extension
    filename=$(basename -- "$file")
    filename="${filename%.*}"

    echo "Processing $file to ui_$filename.py"

    # if an argument --pyside6 is given, use pyside6-uic instead of pyside2-uic
    if [ "$1" = "--pyside6" ]; then
        pyside6-uic "$file" > "ryven/gui/uic/ui_$filename.py"
    else
        pyside2-uic "$file" > "ryven/gui/uic/ui_$filename.py"
    fi

    # replace pyside imports with qtpy
    sed -i 's/from PySide6/from qtpy/g' "ryven/gui/uic/ui_$filename.py"
    sed -i 's/from PySide2/from qtpy/g' "ryven/gui/uic/ui_$filename.py"
done