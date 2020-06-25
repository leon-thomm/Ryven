#include "MainWindow.h"
#include <QApplication>
#include <QFontDatabase>
#include <QDebug>
int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
//    MainWindow w;
//    w.show();

//    return a.exec();
    QFontDatabase db;
    qDebug() << db.families();
}
