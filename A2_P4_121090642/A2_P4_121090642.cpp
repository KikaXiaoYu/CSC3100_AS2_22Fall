
using namespace std;
#include <iostream>

class Node {
public:
    // constructor
    Node() = default;
    Node(int idx, int value):
        idx(idx), value(value),left(NULL), right(NULL) {}

    // setter  
    void setLeft(Node left) {
        this->right = &left;
        left.setParent(*this);
    }
    void setRight(Node right) {
        this->right = &right;
        right.setParent(*this);
    }
    void setIdx(int idx) {
        this->idx = idx; 
    }
    void setValue(int value) {
        this->value = value;
    }

    // getter
    Node getParent() { return *this->parent; }
    Node getLeft() { return *this->left; }
    Node getRight() { return *this->right; }
    int getIdx() { return this->idx; }
    int getValue() { return this->value; }
private:
    int idx;
    int value;
    Node* parent;
    Node* left;
    Node* right;
    // private setter
    void setParent(Node parent) { this->parent = &parent; }
};

// the tree class
class Tree {
public:
    // constructor
    Tree() = default;
    Tree(int size, int min, int max):
        size(size), min(min), max(max) {}

    // getter
    Node getRoot() { return *this->root; }
    int getSize() { return this->size; }
    int getMin() { return this->min; }
    int getMax() { return this->max; }

    // methods
    void insert(int idx, int value) {
        if (this->size == 0) {
            this->root = new Node(idx, value);
        } else {
            int intree_idx = this->min + idx;
            Node cur_node = *this->root;
            int cur_idx = cur_node.getIdx();
            if (intree_idx < cur_idx) { this->min--;}
            if (intree_idx >= cur_idx) { this->max++;}
            while (intree_idx != cur_idx) {
                if (intree_idx < cur_idx) {
                    cur_node = cur_node.getLeft();
                } else {
                    cur_node = cur_node.getRight();
                }
            }
            Node new_node(intree_idx, value);
            cout << "new_node: idx " << new_node.getIdx() << " value " << new_node.getValue()<< endl;
            cur_node.setRight(new_node);
            cout << "set!" << endl;
            cout << cur_node.getRight().getIdx();
            cout << "set finished!" << endl;
        }
        this->size++;
    }
    void printTree(Node cur_node) {
        cout << "!!!" << endl;
        cout << cur_node.getIdx() << endl;
        cout << (cur_node.getLeft()).getIdx() << " ??" << endl;
        
        cout << cur_node.getLeft().getIdx() << " ??" << endl;
        while (cur_node.getLeft().getIdx() != 0 ) {
            cout << "!!!11" << endl;
            printTree(cur_node.getLeft());
        }
        cout << cur_node.getValue() << " ";
        while (cur_node.getRight().getIdx() != 0) {
            cout << "enter!" << endl;
            printTree(cur_node.getRight());
        }
    }

private:
    Node* root;
    int size;
    int min;
    int max;
};


int main() {
    // int line_num;
    // cin >> line_num;
    Tree tree = Tree(0, 0, 0);
    tree.insert(0, 1);
    cout << tree.getMax() << " " << tree.getMin() << " " << tree.getSize() << endl;
    tree.insert(1, 2);
    cout << tree.getMax() << " " << tree.getMin() << " " << tree.getSize() << endl;
    tree.insert(2, 3);
    cout << tree.getMax() << " " << tree.getMin() << " " << tree.getSize() << endl;
    tree.insert(3, 4);
    cout << tree.getMax() << " " << tree.getMin() << " " << tree.getSize() << endl;
    tree.printTree(tree.getRoot());
}