function oddOccurrences(input) {
    // Mask
    let words = {};

    input.split(' ').map((word => word.toLowerCase())).forEach(word => {
        words.hasOwnProperty(word) ? words[word] += 1 : words[word] = 1;
    })

    let result = [];
    for (let [word, count] of Object.entries(words)) {
        count % 2 !== 0 ? result.push(word) : 'pass';
    }

    console.log(result.join(' '));
}

oddOccurrences('Java C# Php PHP Java PhP 3 C# 3 1 5 C#');  // Should return: c# php 1 5
