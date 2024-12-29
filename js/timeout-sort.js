/*
 * Quirky sorting technique that uses javascript's
 * setTimeout function to sort an array
 * of numbers.
 *
 * Written by Samyabrata Maji <samyabratamaji334@gmail.com> (@sammaji)
 */
function sort(inp) {
    inp.forEach(e => {
        setTimeout(() => {
            console.log(e)
        }, e)
    })
}

sort([3,7,2,1,5])
