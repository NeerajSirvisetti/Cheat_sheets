### **HTML5 Cheat Sheet:**

**1. Document Structure:**

   - **HTML Declaration:**
     ```html
     <!DOCTYPE html>
     ```
   - **HTML Root Element:**
     ```html
     <html lang="en">
     ```

**2. Head Section:**

   - **Title Tag:**
     ```html
     <title>Your Title Here</title>
     ```
   - **Meta Tags:**
     ```html
     <meta charset="UTF-8">
     <meta name="viewport" content="width=device-width, initial-scale=1.0">
     ```

**3. Text Formatting:**

   - **Paragraph:**
     ```html
     <p>This is a paragraph.</p>
     ```
   - **Heading Tags:**
     ```html
     <h1>Heading 1</h1>
     <h2>Heading 2</h2>
     <!-- ... -->
     <h6>Heading 6</h6>
     ```
   - **Bold and Italic:**
     ```html
     <strong>Bold Text</strong>
     <em>Italic Text</em>
     ```

**4. Lists:**

   - **Unordered List:**
     ```html
     <ul>
       <li>Item 1</li>
       <li>Item 2</li>
     </ul>
     ```
   - **Ordered List:**
     ```html
     <ol>
       <li>Item 1</li>
       <li>Item 2</li>
     </ol>
     ```
   - **Definition List:**
     ```html
     <dl>
       <dt>Definition Term</dt>
       <dd>Definition Description</dd>
     </dl>
     ```

**5. Links:**

   - **Anchor Tag:**
     ```html
     <a href="https://example.com" target="_blank">Visit Example</a>
     ```

**6. Images:**

   - **Image Tag:**
     ```html
     <img src="image.jpg" alt="Description">
     ```

**7. Forms:**

   - **Form Element:**
     ```html
     <form action="/submit" method="post">
       <!-- Form elements go here -->
     </form>
     ```
   - **Input Fields:**
     ```html
     <input type="text" name="username" placeholder="Username">
     <input type="password" name="password" placeholder="Password">
     ```
   - **Textarea:**
     ```html
     <textarea name="message" rows="4" cols="50">Enter your message here.</textarea>
     ```
   - **Radio Buttons:**
     ```html
     <input type="radio" name="gender" value="male"> Male
     <input type="radio" name="gender" value="female"> Female
     ```
   - **Checkboxes:**
     ```html
     <input type="checkbox" name="subscribe" checked> Subscribe
     ```
   - **Select Dropdown:**
     ```html
     <select name="country">
       <option value="usa">United States</option>
       <option value="canada">Canada</option>
     </select>
     ```

**8. Semantics:**

   - **Header and Footer:**
     ```html
     <header>
       <!-- Header content goes here -->
     </header>
     <footer>
       <!-- Footer content goes here -->
     </footer>
     ```
   - **Section and Article:**
     ```html
     <section>
       <!-- Section content goes here -->
     </section>
     <article>
       <!-- Article content goes here -->
     </article>
     ```
   - **Navigation:**
     ```html
     <nav>
       <!-- Navigation links go here -->
     </nav>
     ```

**9. Multimedia:**

   - **Audio:**
     ```html
     <audio controls>
       <source src="audio.mp3" type="audio/mp3">
       Your browser does not support the audio tag.
     </audio>
     ```
   - **Video:**
     ```html
     <video controls width="320" height="240">
       <source src="video.mp4" type="video/mp4">
       Your browser does not support the video tag.
     </video>
     ```

**10. Tables:**

   - **Table Structure:**
     ```html
     <table>
       <thead>
         <tr>
           <th>Header 1</th>
           <th>Header 2</th>
         </tr>
       </thead>
       <tbody>
         <tr>
           <td>Row 1, Cell 1</td>
           <td>Row 1, Cell 2</td>
         </tr>
         <tr>
           <td>Row 2, Cell 1</td>
           <td>Row 2, Cell 2</td>
         </tr>
       </tbody>
     </table>
     ```

**11. Scripting:**

   - **Script Tag:**
     ```html
     <script>
       // JavaScript code goes here
     </script>
     ```

**12. Styles:**

   - **Internal Styles:**
     ```html
     <style>
       /* CSS styles go here */
     </style>
     ```

**13. Meta Tags:**

   - **Favicons:**
     ```html
     <link rel="icon" href="favicon.ico" type="image/x-icon">
     ```

**14. HTML5 APIs:**

   - **Canvas:**
     ```html
     <canvas id="myCanvas" width="200" height="100"></canvas>
     ```
   - **Geolocation:**
     ```html
     <button onclick="getLocation()">Get Location</button>
     ```

