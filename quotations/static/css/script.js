// script.js

// Initialize current quotation number
let currentQuotationNumber = 1; // Start with 1

// Function to update the Quotation number
function updateQuotationNumber() {
    // Increment the quotation number
    currentQuotationNumber++;
    // Set the new value in the input field
    document.getElementById('quotation-number').value = currentQuotationNumber;
}

// Attach an event listener to the submit button
document.getElementById('submit-button').addEventListener('click', function() {
    // Perform necessary actions before updating the number (like form validation)
    
    // Update the Quotation number
    updateQuotationNumber();

    // You can also add code here to handle form submission, e.g., send data to a server
});
function calculateTotals() {
    const sellingPrice = parseFloat(document.getElementById('selling_price').value) || 0;
    const vat = sellingPrice * 0.1;
    const total = sellingPrice + vat;

    document.getElementById('vat').value = vat.toFixed(2);
    document.getElementById('total').value = total.toFixed(2);
}

function calculateBalance() {
    const total = parseFloat(document.getElementById('total').value) || 0;
    const downpayment = parseFloat(document.getElementById('downpayment').value) || 0;
    const balance = total - downpayment;

    document.getElementById('balance').value = balance.toFixed(2);
}