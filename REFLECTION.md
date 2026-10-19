# Part B: Reflection

### 1. How many tests did you write in Part A, and how many lines of production code? What is the ratio?

I wrote 9 tests and 43 lines of code in Part A. The ratio is 9:43, or about 1 test for every 4.78 lines of code.

### 2. When was your bar red for the longest time, and what made it last so long?

The longest red bar was in A7. It was hard because I had to convert different units. I needed to understand how Quantity, Sum, and Converter work together.

### 3. Find one place where you used Fake It, one where you triangulated, and one where you used Obvious Implementation. Looking back, was each choice right?

I used Fake It in A1 by setting the amount to 600. I used Triangulation in A2 by adding a new test for multiplying by 2. I used Obvious Implementation in A8 to add the times method to Sum.

I think all three were good choices. They helped me write the code step by step.

### 4. Which items are still on your test list? Which would you implement next, and which should you delete because they were speculation?

I finished all 7 items on my test list. Next, I would add tests for wrong inputs and missing conversion rates. I would not add the hash method because I don't need it now.

### 5. Look at Quantity.reduce. If you had designed the whole system on paper first, would you have written this method?

No, I don't think I would have added this method at first. I only thought about adding and multiplying numbers. I added reduce when I needed to work with different units.

### 6. In Part 0 you wrote the tests after the code, and in Part A before it. How did the two feel different, and which tests shaped your design?

In Part 0, I wrote tests to check the code and find bugs. In Part A, I wrote tests first and then wrote the code to pass them.

I think Part A was harder, but it helped me understand TDD better. The tests for multiplication, equality, and unit conversion helped me decide how to write the code.