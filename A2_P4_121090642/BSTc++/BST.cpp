
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
    int getMin() { return this->min; }
    int getMax() { return this->max; }

    // methods
    void insert(int idx, int value) {
        Node new_node(idx, value);
        cout << "address: " << &new_node << endl;
        Node* new_node_p = &new_node;

        new_node_p->setIdx(idx);
        new_node_p->setValue(value);
        cout << "new_node_p->getIdx() " << new_node_p->getIdx() << endl;
        cout << "new_node_p->getValue() " << new_node_p->getValue() << endl;
        cout << "this->root" << this->root << endl;
        if (this->root == NULL) {
            Node root_node;
            this->root = & root_node;
            cout << "root_node.getLeft(): " << root_node.getLeft() << endl; // 0
            cout << "this->root->getLeft(): " << this->root->getLeft() << endl; // 0
            this->root->setIdx(idx);
            this->root->setValue(value);
            cout << "root_node.getLeft(): " << root_node.getLeft() << endl; // 0
        } else {
            Node* cur_node_p = &*this->getRoot();
            cout << "this->root->getLeft(): " << this->root->getLeft() << endl; // 0xa
            cout << "cur_node_p->getLeft(): " << cur_node_p->getLeft() << endl; // 0xa
            Node* last_node_p = this->getRoot();
            int direction;
            int cur_idx;
            while (cur_node_p != NULL) {
                cout << "while (cur_node_p != NULL)" << endl;
                last_node_p = cur_node_p;
                cout << "test11" << endl; 
                cout << "cur_node_p: " << cur_node_p << endl;
                cout << "idx: " << cur_node_p->getIdx();
                cur_idx = cur_node_p->getIdx();
                cout << "test12" << endl; 
                cout << "cur_idx: " << cur_idx << endl;
                cout << "cur_value: " << cur_node_p->getValue() << endl;
                if (idx < cur_idx) {
                    cout << "test1";
                    cur_node_p = cur_node_p->getLeft();
                    cout << "test2";
                    direction = 1;
                } else {
                    cout << "test3";
                    cur_node_p = cur_node_p->getRight();
                    cout << "test4";
                    direction = 2;
                }
            }
            cout << "direction: " << direction << endl;
            if (direction == 1) {
                last_node_p->setLeft(new_node_p);
                cout << "test5";
            } else {
                cout << "address(last)" << &last_node_p << endl;
                cout << "address(curr)" << &cur_node_p << endl;
                last_node_p->setRight(new_node_p);
                cout << "test6";
            }

        }
        cout << "new_node:" << endl;
        cout << "idx(" << new_node_p->getIdx() << ") value(" << new_node_p->getValue()<< ")"<<endl;
        cout << "Finish inserting!" << endl;
        this->size++;
    }


    void printTree(Node* cur_node_p) {
        if (cur_node_p->getLeft() != NULL) {
            cout << "printTree(cur_node_p->getLeft())" << endl;
            printTree(cur_node_p->getLeft());
        }
        cout << cur_node_p->getIdx() << endl;
        if (cur_node_p->getRight() != NULL) {
            cout << "printTree(cur_node_p->getRight())" << endl;
            printTree(cur_node_p->getRight());
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
    cout << "tree.getSize: " << tree.getSize() << endl<< endl;
    tree.insert(1, 2);
    cout << "tree.getSize: " << tree.getSize() << endl<< endl;
    tree.insert(2, 3);
    cout << "tree.getSize: " << tree.getSize() << endl<< endl;
    tree.insert(3, 4);
    cout << "tree.getSize: " << tree.getSize() << endl<< endl;
    tree.printTree(tree.getRoot());
}