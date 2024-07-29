import React from 'react'

function customer_signup() {
  return (
    <div class="container mx-auto mt-4 p-4">
    <h1 class="text-2xl font-bold mb-4">Customer Log In</h1>
    <form method="post" class="space-y-4">
        
        <div class="mb-4">
            <label for="username" class="block text-black-700 font-bold mb-2">Username</label>
            <input type="text" class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="username" name="username" required></input>
        </div>
        <div class="mb-4">
            <label for="password" class="block text-gray-700 font-bold mb-2">Password</label>
            <input type="password" class="shadow appearance-none border rounded w-full py-2 px-3 text-black-700 leading-tight focus:outline-none focus:shadow-outline" id="password" name="password" required></input>
        </div>
        <button type="submit" class="bg-blue-500 text-black font-bold py-2 px-4 rounded hover:bg-blue-700">Sign In</button>
    </form>
</div>
  )
}

export default customer_signup