const readline = require('readline').createInterface({
  input: process.stdin,
  output: process.stdout
});

readline.question('Enter a string: ', (inputString) => {
  const vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'];
  let totalVowels = 0;
  const vowelCounts = {};

  for (const char of inputString) {
    if (vowels.includes(char)) {
      totalVowels++;
      vowelCounts[char] = (vowelCounts[char] || 0) + 1;
    }
  }

  console.log(`Original string: ${inputString}`);
  console.log(`Total number of vowels: ${totalVowels}`);
  console.log('Vowel counts (case-sensitive):');
  for (const vowel in vowelCounts) {
    console.log(`  ${vowel}: ${vowelCounts[vowel]}`);
  }

  readline.close();
});