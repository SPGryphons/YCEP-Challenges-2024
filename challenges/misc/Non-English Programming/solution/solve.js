function secretFunction(code) {
    let result = '';
    for (let i = 0; i < code.length; i++) {
        let charCode = code.charCodeAt(i);
        if (charCode >= 65 && charCode <= 90) {
            result += String.fromCharCode(((charCode - 65 + 13) % 26) + 65);
        } else if (charCode >= 97 && charCode <= 122) {
            result += String.fromCharCode(((charCode - 97 + 13) % 26) + 97);
        } else {
            result += code.charAt(i);
        }
    }
    return result;
}

// Encoded message with the flag is now obfuscated
let obfuscatedMessage = 'LPRC24{Ju4g_N_Ce0te4zz1at_Rkc3eg_L0h_Ne3}';

// Decoding the message to retrieve the flag is now a manual process
// Enter your code here:
let decodedMessage = secretFunction(obfuscatedMessage);
console.log('Decoded Message:', decodedMessage);

console.log('The secret message has been secured.');
