var arrayP = [4,2,3,6,1,10]
calculateMean(arrayP)
function calculateMean(numbers){
    //Get the length of elements in the array
    let numbersLength = numbers.length;
    //to get the sum of all the elements in the list
    let sum = 0;
    //Running the for loop that will add all the elements to the sum
    for(let i = 0; i < numbers.length; i++){
        sum += numbers[i]
    }
    let mean = sum / numbersLength
    console.log("The mean is", mean);
}