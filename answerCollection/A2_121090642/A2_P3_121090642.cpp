
using namespace std;
#include <iostream>
#include <cmath>

// judge that whether it should be removed or not
bool whetherRemove(
    int row, // the row of the judged
    int col,  // the col of the judged
    int rmsize, // square size to be removed
    int rmrow, // remove start row
    int rmcol // remove start col
) {
    // the remove size = 1, if idx not equal to our idx
    // then return false
    if (rmsize == 1 && (row != rmrow || col != rmcol)) {
        return false;
    }
    if ( // the idx is in our remove square and remove size > 1
        row >= rmrow && row < rmrow+rmsize
     && col >= rmcol && col < rmcol+rmsize ) {
        return true;
    } else {
        int nrmsize = rmsize / 3;
        int nrmrow;
        int nrmcol;
        // since remove size > 1, we can recursively get
        // eight small square to move, however, we do not 
        // need to calculate all of them, just one which
        // has the smallest distance to the idx
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
        // judge recursively the smaller remove square
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