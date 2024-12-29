/*
 * Quantum sort
 *
 * This algorithm works by creating a superposition of all possible
 * states and then collapses into a single state based of the
 * probabiliy of a state being
 * sorted.
 *
 * Written by Samyabrata Maji <samyabratamaji334@gmail.com> (@sammaji)
 */
function quantum_sort(arr) {
    const superposition = get_permutations(arr);
    const probability = superposition.map(state => {
        return {
            state,
            amplitude: calculateSortedness(state)
        };
    });

    // return most "probable" (sorted) state
    return probability.reduce((a, b) =>
        a.amplitude > b.amplitude ? a : b
    ).state;
}


/*
 * Calculates "sortedness" - how sorted a given element is.
 * Higher amplitude for more sorted arrays
 */
function calculateSortedness(arr) {
    let sortedness = 0;
    for (let i = 0; i < arr.length - 1; i++) {
        if (arr[i] <= arr[i + 1]) sortedness++;
    }
    return sortedness / (arr.length - 1);
}


function get_permutations(inp) {
  let result = [];

  const permute = (arr, m = []) => {
      if (arr.length === 0) {
          result.push(m);
          return;
    }

      for (let i = 0; i < arr.length; i++) {
          let curr = arr.slice();
          let next = curr.splice(i, 1);
          permute(curr.slice(), m.concat(next));
      }
  }

    permute(inp);
    return result;
}



console.log(quantum_sort([3, 1, 4, 1, 5, 9, 2, 6]));
