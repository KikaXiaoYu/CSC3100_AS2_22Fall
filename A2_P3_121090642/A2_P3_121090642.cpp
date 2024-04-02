
using namespace std;
#include <iostream>
#include <cmath>

// judge that whether it should be removed or not
bool whetherRemove(
    int row, 
    int col, 
    int rmsize,
    int rmrow,
    int rmcol
) { // 
    if (rmsize == 1 && (row != rmrow || col != rmcol)) {
        return false;
    }
    if (
        row >= rmrow && row < rmrow+rmsize
     && col >= rmcol && col < rmcol+rmsize ) {
        return true;
    } else {
        int nrmsize = rmsize / 3;
        int nrmrow;
        int nrmcol;
        if (row < rmrow) {
            nrmrow = rmrow - 2*nrmsize;
        } else if (row >= rmrow && row < rmrow+rmsize) {
            nrmrow = rmrow + 1*nrmsize;
        } else {
            nrmrow = rmrow + 4*nrmsize;
        }
        if (col < rmcol) {
            nrmcol = rmcol - 2*nrmsize;
        } else if (col >= rmcol && col < rmcol+rmsize) {
            nrmcol = rmcol + 1*nrmsize;
        } else {
            nrmcol = rmcol + 4*nrmsize;
        }
        return whetherRemove(row, col, nrmsize, nrmrow, nrmcol);
    }
}

int main() {
    int num;
    int size;
    cin >> num;
    size = pow(3, num);
    for (int row=0; row<size; row++) {
        for (int col=0; col<size; col++) {
            if (whetherRemove(row, col, size/3, size/3, size/3))
                cout << " ";
            else {
                cout << "#";
            }
        }
        cout << endl;
    }
}