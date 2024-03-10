class Node {
    constructor(data) {
        this.data = data;
        this.left = null;
        this.right = null;
    }
}

class BinaryTree {
    constructor() {
        this.root = null;
    }

    insert(data) {
        const newNode = new Node(data);
        if (!this.root) {
            this.root = newNode;
        } else {
            this.insertNode(this.root, newNode);
        }
    }

    insertNode(node, newNode) {
        if (newNode.data < node.data) {
            if (!node.left) {
                node.left = newNode;
            } else {
                this.insertNode(node.left, newNode);
            }
        } else {
            if (!node.right) {
                node.right = newNode;
            } else {
                this.insertNode(node.right, newNode);
            }
        }
    }

    insertLeft(data) {
        const newNode = new Node(data);
        if (!this.root) {
            this.root = newNode;
        } else {
            this.insertLeftNode(this.root, newNode);
        }
    }

    insertLeftNode(node, newNode) {
        if (!node.left) {
            node.left = newNode;
        } else {
            this.insertLeftNode(node.left, newNode);
        }
    }

    insertRightEnd(data) {
        const newNode = new Node(data);
        if (!this.root) {
            this.root = newNode;
        } else {
            this.insertRightNodeEnd(this.root, newNode);
        }
    }

    insertRightNodeEnd(node, newNode) {
        if (node.left) {
            this.insertRightNodeEnd(node.left, newNode);
        } else {
            if (!node.right) {
                node.right = newNode;
            } else {
                this.insertRightNodeEnd(node.right, newNode);
            }
        }
    }


    search(word) {
        return this.searchNode(this.root, word);
    }

    searchNode(node, word) {
        if (!node) {
            return false;
        }
        if (word === node.data) {
            return true;
        }
        if (word < node.data) {
            return this.searchNode(node.left, word);
        }
        return this.searchNode(node.right, word);
    }
}