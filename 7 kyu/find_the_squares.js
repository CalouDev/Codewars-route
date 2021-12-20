// I made it in JavaScript because, in Python, the script was too slow

const findSquares = num => {
  multiply = 1;
  while (Math.pow(multiply+1, 2) - Math.pow(multiply, 2) != num) { multiply++; }
  return `${Math.pow(multiply+1, 2)}-${Math.pow(multiply, 2)}`
};
