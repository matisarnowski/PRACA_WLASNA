#include <iostream>
#include <iomanip>
#include <new>

using namespace std;

int main()
{
    const size_t mega = 1024*1024, step = 200*mega;

    //cout << sizeof(size_t(mega)) << endl;

    for(size_t size = step ;; size += step){
        try {
            char* buf = new char[size];
            delete [] buf;
        } catch (bad_alloc){
            cout << "Nie udalo sie zalokowac: " << setw(6) << size/mega << " MB." << endl;
            return 1;
        } cout << "Udalo sie zalokowac: " << setw(6) << size/mega << " MB." << endl;
    }
}