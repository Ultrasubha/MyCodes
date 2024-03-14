function outerExample() {
    s = "what is this braaaaaawwwwwww"
    function innerExample() {
        return s
    }
    return innerExample()
}

console.log(outerExample())