### **CSS Cheat Sheet:**

**1. Selectors:**

   - **Universal Selector:**
     ```css
     * {
       /* styles apply to all elements */
     }
     ```
   - **Type Selector:**
     ```css
     p {
       /* styles apply to all <p> elements */
     }
     ```
   - **Class Selector:**
     ```css
     .className {
       /* styles apply to elements with class="className" */
     }
     ```
   - **ID Selector:**
     ```css
     #elementID {
       /* styles apply to element with id="elementID" */
     }
     ```
   - **Descendant Selector:**
     ```css
     div p {
       /* styles apply to <p> inside <div> */
     }
     ```
   - **Attribute Selector:**
     ```css
     input[type="text"] {
       /* styles apply to text input elements */
     }
     ```

**2. Box Model:**

   - **Width and Height:**
     ```css
     .box {
       width: 200px;
       height: 100px;
     }
     ```
   - **Padding:**
     ```css
     .box {
       padding: 10px;
     }
     ```
   - **Margin:**
     ```css
     .box {
       margin: 10px;
     }
     ```
   - **Border:**
     ```css
     .box {
       border: 1px solid #000;
     }
     ```

**3. Positioning:**

   - **Relative Positioning:**
     ```css
     .relative {
       position: relative;
       top: 10px;
       left: 20px;
     }
     ```
   - **Absolute Positioning:**
     ```css
     .absolute {
       position: absolute;
       top: 30px;
       right: 10px;
     }
     ```
   - **Fixed Positioning:**
     ```css
     .fixed {
       position: fixed;
       bottom: 0;
       right: 0;
     }
     ```

**4. Flexbox:**

   - **Container:**
     ```css
     .flex-container {
       display: flex;
       justify-content: space-between;
     }
     ```
   - **Items:**
     ```css
     .flex-item {
       flex: 1;
     }
     ```

**5. Grid:**

   - **Container:**
     ```css
     .grid-container {
       display: grid;
       grid-template-columns: auto auto auto;
     }
     ```
   - **Items:**
     ```css
     .grid-item {
       grid-column: span 2;
     }
     ```

**6. Typography:**

   - **Font Family:**
     ```css
     body {
       font-family: "Arial", sans-serif;
     }
     ```
   - **Font Size:**
     ```css
     h1 {
       font-size: 24px;
     }
     ```
   - **Font Weight:**
     ```css
     p {
       font-weight: bold;
     }
     ```

**7. Colors and Backgrounds:**

   - **Color:**
     ```css
     .text-red {
       color: red;
     }
     ```
   - **Background Color:**
     ```css
     .bg-blue {
       background-color: blue;
     }
     ```

**8. Transitions and Animations:**

   - **Transition:**
     ```css
     .transition {
       transition: width 0.5s ease-in-out;
     }
     ```
   - **Keyframe Animation:**
     ```css
     @keyframes slide {
       from {
         transform: translateX(-100%);
       }
       to {
         transform: translateX(0);
       }
     }
     ```

**9. Responsive Design:**

   - **Media Queries:**
     ```css
     @media screen and (max-width: 600px) {
       /* styles for screens up to 600px wide */
     }
     ```

**10. Pseudo-classes and Pseudo-elements:**

   - **Hover:**
     ```css
     a:hover {
       color: #ff0000;
     }
     ```
   - **First-child:**
     ```css
     li:first-child {
       font-weight: bold;
     }
     ```
   - **Before Pseudo-element:**
     ```css
     .box::before {
       content: "Before";
       color: #000;
     }
     ```

**11. Flexbox:**

   - **Container:**
     ```css
     .flex-container {
       display: flex;
       justify-content: space-between;
     }
     ```
   - **Items:**
     ```css
     .flex-item {
       flex: 1;
     }
     ```

**12. Responsive Design:**

   - **Media Queries:**
     ```css
     @media screen and (max-width: 600px) {
       /* styles for screens up to 600px wide */
     }
     ```

**13. CSS Variables:**

   - **Declaration:**
     ```css
     :root {
       --main-color: #3498db;
     }
     ```
     ```css
     .element {
       background-color: var(--main-color);
     }
     ```

