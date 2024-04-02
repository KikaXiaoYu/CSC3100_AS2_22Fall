
using namespace std;
#include <iostream>

class Node {
public:
    // constructor
    Node():
         idx(0), value(0){}
    Node(int idx, int value):
        idx(idx), value(value){}

    // setter  
    void setLeft(Node* left) { // a pointer
        cout << "test7";
        this->right = left;
        cout << "test8";
        left->setParent(this);
    }
    void setRight(Node* right) {
        cout << "test9";
        this->right = right;
        cout << "test10";
        right->setParent(this);
    }
    void setIdx(int idx) {
        this->idx = idx; 
    }
    void setValue(int value) {
        this->value = value;
    }

    // getter
    Node* getParent() { return this->parent; }
    Node* getLeft() { 
        return this->left; 
    }
    Node* getRight() {
        return this->right;
        }
    int getIdx() { return this->idx; }
    int getValue() { return this->value; }

private:
    int idx;
    int value;
    Node* parent;
    Node* left;
    Node* right;
    // private setter
    void setParent(Node* parent) {
        this->parent = parent;
    }
};

// the tree class
class Tree {
public:
    // constructor
    Tree(int size, int min, int max):
        size(size), min(min), max(max), root(NULL) {}
    // getter
    Node* getRoot() { return this->root; }
    int getSize() { return this->size; }
    // methods

    void insert(int idx, int value) {

        Node new_node(idx, value);
        Node* new_node_p = &new_node;
        new_node_p->setIdx(idx);
        new_node_p->setValue(value);
        // cout << "new_node_p->getIdx() " << new_node_p->getIdx() << endl;
        // cout << "new_node_p->getValue() " << new_node_p->getValue() << endl;
        if (this->root == NULL) {
            cout << "if (this->root == NULL)" << endl;
            Node root_node;
            this->root = & root_node;
            cout << "root_node.getLeft(): " << root_node.getLeft() << endl; // 0
            cout << "this->root->getLeft(): " << this->root->getLeft() << endl; // 0
            this->root->setIdx(idx);
            this->root->setValue(value);
            cout << "root_node.getLeft(): " << root_node.getLeft() << endl; // 0
            cout << "this->root->getLeft(): " << this->root->getLeft() << endl; // 0
        } else {
            cout << "else" << endl;
            Node* cur_node_p = this->root;
            cout << "this->root->getLeft(): " << this->root->getLeft() << endl; // 0xa
            cout << "cur_node_p->getLeft(): " << cur_node_p->getLeft() << endl; // 0xa
        }
    }

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
    tree.insert(1, 2);
}