function reverseWords(s) {
  const resArr = []
  let l = 0
  let r = 0
  for (let i = 0; i < s.length; i++) {
    if (s.charAt(r) !== ' ') {
      r += 1
    } else {
      let slice = s.slice(l, r).split('').reverse().join('');
      resArr.push(slice);
      r += 1;
      l = r;
    }
  }
  let slice = s.slice(l, r).split('').reverse().join('');
  resArr.push(slice);
  return resArr.join(' ');
};