# Database Concepts Cheatsheet
## ACID
ACID stands for Atomicity, Consistency, Isolation, and Durability. It is a set of properties that guarantee that database transactions are processed reliably.

**Atomicity:** Ensures that a transaction is treated as a single, indivisible unit, either fully completed or fully rolled back.<br>
**Consistency:** Ensures that a transaction brings a database from one valid state to another, maintaining data integrity constraints.<br>
**Isolation:** Guarantees that the execution of transactions is isolated from each other, preventing interference between them.<br>
**Durability:** Ensures that once a transaction is committed, its changes are permanent and survive system failures.

## CAP Theorem
CAP theorem states that a distributed system cannot simultaneously provide more than two out of three guarantees: Consistency, Availability, and Partition tolerance.

**Consistency:** All nodes in the system see the same data at the same time.<br>
**Availability:** Every request to a non-failing node in the system receives a response without guarantee that it contains the most recent version of the data.<br>
**Partition Tolerance:** The system continues to operate despite network partitions or communication failures.

## Joins
Joins combine rows from two or more tables based on related columns.

**Inner Join:** Returns only the rows where there is a match in both tables.<br>
**Left Join (or Left Outer Join):** Returns all rows from the left table and matching rows from the right table.<br>
**Right Join (or Right Outer Join):** Returns all rows from the right table and matching rows from the left table.<br>
**Full Join (or Full Outer Join):** Returns all rows when there is a match in either table.

## Aggregations, Filters in queries
### Aggregations
It perform operations on a set of values, often grouped together.

**COUNT:** Returns the number of rows in a table.<br>
**SUM:** Returns the sum of values in a column.<br>
**AVG:** Returns the average of values in a column.<br>
**MIN/MAX:** Returns the minimum/maximum value in a column.

### Filters 
It restrict the result set based on specified conditions.

**WHERE:** Filters rows based on a condition.<br>
**GROUP BY:** Groups rows that have the same values in specified columns.<br>
**HAVING:** Filters groups based on conditions after the GROUP BY clause.

## Normalization
Normalization is the process of organizing data in a database to eliminate redundancy and dependency.

**First Normal Form (1NF):** Eliminates duplicate columns from the same table.<br>
**Second Normal Form (2NF):** 1NF + no partial dependencies on a candidate key.<br>
**Third Normal Form (3NF):** 2NF + no transitive dependencies.

## Indexes
Indexes improve the speed of data retrieval operations on a database table.

**Clustered Index:** Determines the physical order of data rows in a table.<br>
**Non-clustered Index:** Creates a separate structure storing a sorted subset of the data.

## Transactions
A transaction is a sequence of one or more SQL statements executed as a single unit of work.

**Begin Transaction:** Starts a transaction.<br>
**Commit:** Saves the changes made during the transaction.<br>
**Rollback:** Undoes the changes made during the transaction.

## Locking mechanism
Locks control access to a database, preventing multiple users from accessing the same data simultaneously.

**Shared Lock:** Allows multiple transactions to read a resource but prevents any from writing to it.<br>
**Exclusive Lock:** Allows only one transaction to access a resource for writing.<br>
**Read Lock/Write Lock:** More granular than shared/exclusive locks, allowing different types of access.

## Database Isolation Levels
Isolation levels define the extent to which a transaction is isolated from the effects of other concurrent transactions.

**Read Uncommitted:** Allows transactions to read uncommitted changes.<br>
**Read Committed:** Ensures a transaction sees only committed changes.<br>
**Repeatable Read:** Prevents other transactions from updating or inserting rows being read.<br>
**Serializable:** Ensures transactions are executed in a way that is indistinguishable from a serial execution.

## Triggers
Triggers are sets of instructions that are automatically executed in response to certain events on a particular table or view.

**BEFORE Trigger:** Executes before the operation.<br>
**AFTER Trigger:** Executes after the operation.<br>
**INSTEAD OF Trigger:** Replaces the original operation with the trigger's action.