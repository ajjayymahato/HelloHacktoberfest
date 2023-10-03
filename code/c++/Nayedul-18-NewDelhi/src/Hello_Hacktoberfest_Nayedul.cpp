#include <iostream>
using namespace std;

int main(int argc, char const *argv[])
{
    int userInput;

    cout << "Enter your preferred language (English[1], Hindi[2], Spanish[3], French[4] or German[5]): ";
    cin >> userInput;

    if (userInput == 1) {
        cout << "Hello Hacktoberfest!" << endl;
    } else if (userInput == 2) {
        cout << "Namaste Hacktoberfest!" << endl;
    } else if (userInput == 3) {
        cout << "Hola Hacktoberfest!" << endl;
    } else if (userInput == 4) {
        cout << "Bonjour Hacktoberfest!" << endl;
    } else if (userInput == 5) {
        cout << "Hallo  Hacktoberfest!" << endl;
    } else {
        cout << "Sorry, we don't support that language." << endl;
    }


    return 0;
}
