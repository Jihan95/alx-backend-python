Python - Async

async and await syntax
The async and await syntax in Python is used to write asynchronous code, which allows your program to perform non-blocking operations, such as waiting for I/O tasks (like reading from a file, making a network request, etc.), while still being able to do other things.
async keyword
Purpose: async is used to define a coroutine. A coroutine is a special type of function that can pause and resume its execution, allowing other code to run in the meantime.
How to Use: You place async before the def keyword when defining a function
await keyword
Purpose: await is used to pause the execution of the coroutine until the awaited asynchronous task completes. It is only valid inside an async function.

How to Use: You place await before a function call that returns a coroutine or an awaitable (something that can be awaited, like an asyncio task).

How to execute an async program with asyncio
To execute an async program using asyncio, you generally follow these steps:
Define your coroutines using async def.
Use await to call other coroutines or awaitable objects within your coroutines.
Run your async program using asyncio.run().

How to run concurrent coroutines
Using asyncio.create_task or asyncio.gather

How to create asyncio tasks
asyncio.create_task() to schedule coroutines to run concurrently and then await them later.
