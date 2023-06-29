## OOP - Object Oriented Programming

1.  Class variables
2.  Methods - functions written within the classes - types of methods:
    i) Instance methods - have 'self' as the default input argument
    ii) Static methods - Doesn't have any default input argument. - created loosely, or using decorator @staticmethod
    iii) class methods

### OOP

    - Data binding (variables and methods)
    - encapsulation
        - data hiding
        - public/protected/private
    - Inheritance
        1. single Inheritance
        2. Multiple Inheritance
            (i) Diamond Inheritance
    - Polymorphism - overloading
        1 + 2           addition
        '1' + '2'       string concatenation
        [1, 2] + [2]    list concatenation

### Class Responsibility Collaboration (CRC) cards

    - These cards help identify and define the responsibilities of each class in a system, as well as how they collaborate and interact with other classes.
    - Concept is to represent classes on index cards or small piece of paper.
    - Each card represents a single class and contains the following information:
        1) Class name       : The name of the class.
        2) responsibilities : The specific tasks or responsibilities that the class is responsible for.
        3) Collaborators    : Other classes or objects that the class collaborates with to fulfill its responsibilities.

    - Example

        ----------------------------------------------------
        |                  Order                           |
        |--------------------------------------------------|
        | - customer: Customer                             |
        | - items: List<Item>                              |
        |--------------------------------------------------|
        | + addItems(items: List<Item>): void              |
        | + removeItem(item: Item): void                   |
        | + calculateTotal(): double                       |
        | + placeOrder(): void                             |
        ----------------------------------------------------

        ----------------------------------------------------
        |                Customer                          |
        |--------------------------------------------------|
        | - name: string                                   |
        | - address: string                                |
        |--------------------------------------------------|
        | + getName(): string                              |
        | + getAddress(): string                           |
        ----------------------------------------------------

        ----------------------------------------------------
        |                 Item                             |
        |--------------------------------------------------|
        | - name: string                                   |
        | - price: double                                  |
        |--------------------------------------------------|
        | + getName(): string                              |
        | + getPrice(): double                             |
        ----------------------------------------------------

### User Diagram (or) Use-Case Diagram

    - Its a type of behavioral diagram in Unified Modelling Language(UML)
    - visual representation that depicts the interactions between actors (users or external systems) and a system
    - Used to understand and document functionality of system from a user's perspective
    - Benifits
        - Visualizing User Interactions
        - Identifying Use Cases
        - Clarifying System Boundaries
        - Communication and Collaboration
        - Requirements Analysis
        - Basis for Testing and Validation

    - Example
                    +------------------------+
                    |   Online Shopping      |
                    +------------------------+
                            |
                            | (1) Browse products
                            v
                    +------------------------+
                    |   Customer             |
                    +------------------------+
                            |
                            | (2) Add to cart
                            v
                    +------------------------+
                    |   Shopping Cart        |
                    +------------------------+
                            |
                            | (3) Proceed to checkout
                            v
                    +------------------------+
                    |   Payment              |
                    +------------------------+
                            |
                            | (4) Confirm purchase
                            v
                    +------------------------+
                    |   Order Processing     |
                    +------------------------+
                            |
                            | (5) Send order confirmation
                            v
                    +------------------------+
                    |   Email Service        |
                    +------------------------+
