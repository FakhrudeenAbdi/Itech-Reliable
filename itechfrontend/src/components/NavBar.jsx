import React from 'react';
import { Link } from 'react-router-dom';

function NavBar() {
  return (
    <nav className="bg-primary py-4 text-white">
      <div className="container mx-auto flex justify-between items-center">
        <Link to="/" className="text-2xl font-bold">
          Itech Reliable
        </Link>
        <ul className="flex space-x-4">
          <li>
            <Link to="/" className="hover:text-gray-300">
              Home
            </Link>
          </li>
          <li>
            <Link to="/plans" className="hover:text-gray-300">
              Plans
            </Link>
          </li>
          <li>
            <Link to="/signup" className="hover:text-gray-300">
              Signup
            </Link>
          </li>
        </ul>
      </div>
    </nav>
  );
}

export default NavBar;