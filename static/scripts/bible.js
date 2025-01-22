// List of books and the approximate maximum chapters in each book.
const bibleBooks = [
    { name: "Genesis", chapters: 50 },
    { name: "Exodus", chapters: 40 },
    { name: "Leviticus", chapters: 27 },
    { name: "Numbers", chapters: 36 },
    { name: "Deuteronomy", chapters: 34 },
    { name: "Joshua", chapters: 24 },
    { name: "Judges", chapters: 21 },
    { name: "Ruth", chapters: 4 },
    { name: "1 Samuel", chapters: 31 },
    { name: "2 Samuel", chapters: 24 },
    { name: "1 Kings", chapters: 22 },
    { name: "2 Kings", chapters: 25 },
    { name: "1 Chronicles", chapters: 29 },
    { name: "2 Chronicles", chapters: 36 },
    { name: "Ezra", chapters: 10 },
    { name: "Nehemiah", chapters: 13 },
    { name: "Esther", chapters: 10 },
    { name: "Job", chapters: 42 },
    { name: "Psalms", chapters: 150 },
    { name: "Proverbs", chapters: 31 },
    { name: "Ecclesiastes", chapters: 12 },
    { name: "Song of Solomon", chapters: 8 },
    { name: "Isaiah", chapters: 66 },
    { name: "Jeremiah", chapters: 52 },
    { name: "Lamentations", chapters: 5 },
    { name: "Ezekiel", chapters: 48 },
    { name: "Daniel", chapters: 12 },
    { name: "Hosea", chapters: 14 },
    { name: "Joel", chapters: 3 },
    { name: "Amos", chapters: 9 },
    { name: "Obadiah", chapters: 1 },
    { name: "Jonah", chapters: 4 },
    { name: "Micah", chapters: 7 },
    { name: "Nahum", chapters: 3 },
    { name: "Habakkuk", chapters: 3 },
    { name: "Zephaniah", chapters: 3 },
    { name: "Haggai", chapters: 2 },
    { name: "Zechariah", chapters: 14 },
    { name: "Malachi", chapters: 4 },
    { name: "Matthew", chapters: 28 },
    { name: "Mark", chapters: 16 },
    { name: "Luke", chapters: 24 },
    { name: "John", chapters: 21 },
    { name: "Acts", chapters: 28 },
    { name: "Romans", chapters: 16 },
    { name: "1 Corinthians", chapters: 16 },
    { name: "2 Corinthians", chapters: 13 },
    { name: "Galatians", chapters: 6 },
    { name: "Ephesians", chapters: 6 },
    { name: "Philippians", chapters: 4 },
    { name: "Colossians", chapters: 4 },
    { name: "1 Thessalonians", chapters: 5 },
    { name: "2 Thessalonians", chapters: 3 },
    { name: "1 Timothy", chapters: 6 },
    { name: "2 Timothy", chapters: 4 },
    { name: "Titus", chapters: 3 },
    { name: "Philemon", chapters: 1 },
    { name: "Hebrews", chapters: 13 },
    { name: "James", chapters: 5 },
    { name: "1 Peter", chapters: 5 },
    { name: "2 Peter", chapters: 3 },
    { name: "1 John", chapters: 5 },
    { name: "2 John", chapters: 1 },
    { name: "3 John", chapters: 1 },
    { name: "Jude", chapters: 1 },
    { name: "Revelation", chapters: 22 }
  ];
  
  // Function to get a random Bible verse
  const getRandomBibleVerse = async (translation = "kjv") => {
    // Select a random book
    const randomBook = bibleBooks[Math.floor(Math.random() * bibleBooks.length)];
    
    // Select a random chapter from the book
    const randomChapter = Math.floor(Math.random() * randomBook.chapters) + 1;
    
    // API URL for the selected book and chapter
    const apiUrl = `https://bible-api.com/${randomBook.name}+${randomChapter}`;
    
    try {
      const response = await fetch(apiUrl);
      const data = await response.json();
  
      // Check if the response contains verses
      if (data.verses && data.verses.length > 0) {
        // Select a random verse from the chapter
        const randomVerse = data.verses[Math.floor(Math.random() * data.verses.length)];
        
        // Display the result
        console.log(`Verse: ${randomVerse.text.trim()}`);
        console.log(`Reference: ${randomVerse.book_name} ${randomVerse.chapter}:${randomVerse.verse}`);
      } else {
        console.error("No verses found for the selected chapter.");
      }
    } catch (error) {
      console.error("Error fetching Bible verse:", error);
    }
  };
  
  // Run the function to fetch a random verse (default translation: KJV)

  
document.addEventListener("DOMContentLoaded", function() {
    // Run the function to fetch a random verse
    getRandomBibleVerse("esv"); // Change "esv" to your preferred translation if needed
});
