/* Problem -> https://www.hackerrank.com/challenges/js10-let-and-const/problem */

function main() {
    // Write your code here. Read input using 'readLine()' and print output using 'console.log()'.
    let r = Number(readLine())
    // Print the area of the circle:
    let area = (r ** 2) * Math.PI
    console.log(area)
    // Print the perimeter of the circle:
    const perimeter = 2 * Math.PI * r 
    console.log(perimeter)

