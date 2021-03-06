// There are two ways to test the task in Judge
// This is the new way:
function forecast2(temperature) {
    if (26.00 <= temperature && temperature <= 35.00) {
        console.log("Hot");
    } else if (20.1 <= temperature && temperature <= 25.9) {
        console.log("Warm");
    } else if (15.00 <= temperature && temperature <= 20.00) {
        console.log("Mild");
    } else if (12.00 <= temperature && temperature <= 14.9) {
        console.log("Cool");
    } else if (5.00 <= temperature && temperature <= 11.9) {
        console.log("Cold");
    } else {
        console.log("unknown");
    }
}
forecast2(16.5);  // Expected output: Mild
forecast2(8);  // Expected output: Cold
forecast2(22.4);  // Expected output: Warm
forecast2(26);  // Expected output: Hot
forecast2(0);  // Expected output: unknown


// -----------------------------------------------------------------------------------//
// Old way of reading the input:
function forecast2Old(input) {
    let temperature = Number(input.shift());
    if (26.00 <= temperature && temperature <= 35.00) {
        console.log("Hot");
    } else if (20.1 <= temperature && temperature <= 25.9) {
        console.log("Warm");
    } else if (15.00 <= temperature && temperature <= 20.00) {
        console.log("Mild");
    } else if (12.00 <= temperature && temperature <= 14.9) {
        console.log("Cool");
    } else if (5.00 <= temperature && temperature <= 11.9) {
        console.log("Cold");
    } else {
        console.log("unknown");
    }
}

forecast2Old([16.5]);  // Expected output: Mild
forecast2Old([8]);  // Expected output: Cold
forecast2Old([22.4]);  // Expected output: Warm
forecast2Old([26]);  // Expected output: Hot
forecast2Old([0]);  // Expected output: unknown
