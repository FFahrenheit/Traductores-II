const inputControl = document.getElementById('tree_input');
const run = document.getElementById('run_button');
const treeCanvas = document.getElementById('tree_canvas');
const inputCanvas = document.getElementById('input_canvas');
const treeCtx = treeCanvas.getContext('2d');
const inputCtx = inputCanvas.getContext('2d');

const words =  ["if", "else", "while", "for", "int", "float", "void", "char", "return", "break"];
const drawTree = (node, x, y, dx, ctx) => {
    if (node) {
        ctx.beginPath();
        ctx.arc(x, y, 20, 0, 2 * Math.PI);
        ctx.stroke();
        ctx.fillText(node.data, x - 10, y + 5);
        if (node.left !== null) {
            ctx.moveTo(x, y + 20);
            ctx.lineTo(x - dx, y + 50);
            ctx.stroke();
            drawTree(node.left, x - dx, y + 50, dx / 2, ctx);
        }
        if (node.right !== null) {
            ctx.moveTo(x, y + 20);
            ctx.lineTo(x + dx, y + 50);
            ctx.stroke();
            drawTree(node.right, x + dx, y + 50, dx / 2, ctx);
        }
    }
};
const tree = new BinaryTree();

(() => {
    words.forEach(word => {
        tree.insert(word);
    });
    drawTree(tree.root, treeCanvas.width / 2, 50, treeCanvas.width / 4, treeCtx);
})();

run.addEventListener('click', (e) => {
    e.preventDefault();
    inputCtx.clearRect(0, 0, inputCanvas.width, inputCanvas.height);
    const input = inputControl.value;
    const searchTree = new BinaryTree();
    let currentInput = "";
    let lastMatch = "";

    for (let char of input) {
        currentInput += char;
        if (words.some(word => word.startsWith(currentInput))) {
            lastMatch = currentInput;
        } else {
            break;
        }
    }
    const found = words.find(word => lastMatch && word.startsWith(lastMatch));
    console.log({
        currentInput, lastMatch, found
    })

    if (found) {
        if (found == input) {
            for (char of input) {
                searchTree.insertLeft(char);
            }
        } else {
            for (char of lastMatch) {
                searchTree.insertLeft(char);
            }
            for (let i = lastMatch.length; i < input.length; i++) {
                searchTree.insertRightEnd(input[i]);
            }
            for (let i = lastMatch.length; i < found.length; i++) {
                searchTree.insertLeft(found[i]);
            }
        }
    } else {
        for (char of input) {
            searchTree.insertRightEnd(char);
        }
    }
    drawTree(searchTree.root, inputCanvas.width / 2, 50, inputCanvas.width / 4, inputCtx);

});