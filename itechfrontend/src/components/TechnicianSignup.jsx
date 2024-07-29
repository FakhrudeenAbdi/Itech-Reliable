import React from 'react';

function TechnicianSignup() {
  return (
    <div className="container mx-auto my-10">
      <h1 className="text-3xl font-bold mb-5">Technician Signup</h1>
      <form className="bg-white rounded-lg shadow-md p-6">
        {/* Your form fields here */}
        <div className="mb-4">
          <label htmlFor="name" className="block font-bold mb-2">
            Name
          </label>
          <input
            type="text"
            id="name"
            name="name"
            className="border rounded-md py-2 px-3 w-full"
            required
          />
        </div>
        <div className="mb-4">
          <label htmlFor="email" className="block font-bold mb-2">
            Email
          </label>
          <input
            type="email"
            id="email"
            name="email"
            className="border rounded-md py-2 px-3 w-full"
            required
          />
        </div>
        {/* Add more form fields as needed */}
        <button type="submit" className="bg-primary text-white font-bold py-2 px-4 rounded-md">
          Sign Up
        </button>
      </form>
    </div>
  );
}

export default TechnicianSignup;