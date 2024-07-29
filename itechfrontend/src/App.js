import './App.css';
import React from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import TechnicianSignup from './components/TechnicianSignup';
import AdministratorSignup from './components/administrator_signup';
import CustomerRegister from './components/customer_register';
import CustomerSignup from './components/customer_signup';
import PlanDetail from './components/plan_detail';
import Plans from './components/plans';
// import NavBar from './components/NavBar';
import CustomerDashboard from './components/CustomerDashboard';
import itechProfileImage from './assets/itech profile-pages-images-0.jpg';
import itechProfileImage1 from './assets/itech profile-pages-images-1.jpg';
import itechProfileImage2 from './assets/itech profile-pages-images-2.jpg';
import itechProfileImage3 from './assets/itech profile-pages-images-3 edited.jpg';
import itechProfileImage9 from './assets/itech profile-pages-images-9.jpg';

function App() {
  return (
<Router>
      <div className="flex flex-col min-h-screen">
        
        {/* Header */}
        <header className="bg-primary py-4 text-black">
          <nav className="container mx-auto flex justify-between items-center">
            <Link to="/" className="text-2xl font-bold">
              Itech Reliable
            </Link>
            <ul className="flex space-x-4">
              <li>
                <Link to="/" className="hover:text-black-300">
                  Home
                </Link>
              </li>
              <li>
                <Link to="/plans" className="hover:text-black-300">
                  Plans
                </Link>
              </li>
              <li>
                <Link to="/customer-signup" className="hover:text-black-300">
                  Signup
                </Link>
              </li>
              <li>
              <Link to="/customer-dashboard">Customer Dashboard</Link>
            </li>
            </ul>
          </nav>
        </header>
        {/* Main Content */}
        <main className="flex-1">
          <Routes>
            <Route path="/plans" element={<Plans />} />
            <Route path="/technician-signup" element={<TechnicianSignup />} />
            <Route path="/administrator-signup" element={<AdministratorSignup />} />
            <Route path="/customer-register" element={<CustomerRegister />} />
            <Route path="/customer-signup" element={<CustomerSignup />} />
            <Route path="/plan-detail" element={<PlanDetail />} />

            <Route path="/" element={
              <div className="container mx-auto">
              {/*  Header Section  */}
              {/* <img src="{% public 'images/itechfrontend/public/itech profile-pages-images-0.jpg' %}" alt="About Us" className="img-fluid rounded" /> */}
              <img src={itechProfileImage} alt="Itech Profile Image" className="img-fluid rounded"/>
              <header className="bg-primary py-5 text-center">
                <div className="container mx-auto">
                  <h1 className="text-white text-4xl font-bold">Itech Reliable</h1>
                  <p className="text-white text-xl">Managing Your Internet Needs Efficiently</p>
                  <a href="{% url 'plans' %}" className="btn bg-white text-primary font-bold py-2 px-4 rounded mt-3">View Plans</a>
                </div>
              </header>
        
              {/* About Section  */}
              <section className="py-5">
                <div className="container mx-auto">
                  <div className="flex flex-col md:flex-row items-center">
                    <div className="md:w-1/2">
                    <img src={itechProfileImage1} alt="Itech Profile Image" className="img-fluid rounded"/>
                    </div>
                    <div className="md:w-1/2 md:ml-8">
                      <h2 className="text-2xl font-bold">About Us</h2>
                      <p className="text-lg">We provide the best internet services with reliable support.</p>
                      <p>Our mission is to deliver high-speed internet with unmatched customer service. Whether you're at home or work, our network is designed to meet all your needs.</p>
                    </div>
                  </div>
                </div>
              </section>
              <img src={itechProfileImage3} alt="Itech Profile Image" className="img-fluid rounded"/>
              {/*  Features Section  */}
              <section className="bg-gray-100 py-5">
                <div className="container mx-auto">
                  <h2 className="text-center text-2xl font-bold mb-5">Our Features</h2>
                  <img src={itechProfileImage2} alt="Itech Profile Image" className="img-fluid rounded"/>
                  <div className="flex flex-wrap justify-center">
                    <div className="w-full md:w-1/3 text-center mb-5">
                      <div className="p-4">
                        <i className="fas fa-wifi fa-3x mb-3 text-primary"></i>
                        <h4 className="text-xl font-bold">High-Speed Internet</h4>
                        <p>Experience lightning-fast speeds for all your needs.</p>
                      </div>
                    </div>
                    <div className="w-full md:w-1/3 text-center mb-5">
                      <div className="p-4">
                        <i className="fas fa-shield-alt fa-3x mb-3 text-primary"></i>
                        <h4 className="text-xl font-bold">Secure Connection</h4>
                        <p>Your security is our priority with our robust network.</p>
                      </div>
                    </div>
                    <div className="w-full md:w-1/3 text-center mb-5">
                      <div className="p-4">
                        <i className="fas fa-headset fa-3x mb-3 text-primary"></i>
                        <h4 className="text-xl font-bold">24/7 Support</h4>
                        <p>We're here to help anytime you need us.</p>
                      </div>
                    </div>
                  </div>
                </div>
              </section>
        
              {/*  Plans Section  */}
              <section className="py-5">
                <div className="container mx-auto">
                  <h2 className="text-center text-2xl font-bold mb-5">Our Plans</h2>
                  <div className="flex flex-wrap">
                    <div className="w-full md:w-1/4 p-2">
                      <div className="border rounded-lg p-4 bg-white shadow-md">
                        <h5 className="text-xl font-bold">8 Mbps</h5>
                        <p>Fast web browsing</p>
                        <p>SD Movie & music streaming</p>
                        <p>SD TV programming</p>
                        <p>CCTV devices Capability</p>
                        <p>Multiple device streaming</p>
                        <p>Superfast video downloads</p>
                        <p className="font-bold">Kshs 2500 for 30 days</p>
                      </div>
                    </div>
                    <div className="w-full md:w-1/4 p-2">
                      <div className="border rounded-lg p-4 bg-white shadow-md">
                        <h5 className="text-xl font-bold">10 Mbps</h5>
                        <p>HD streaming</p>
                        <p>YouTube streaming</p>
                        <p>CCTV cameras</p>
                        <p>Movie download</p>
                        <p>Online video streaming</p>
                        <p>Multiple device streaming</p>
                        <p className="font-bold">Kshs 3500 for 30 days</p>
                      </div>
                    </div>
                    <div className="w-full md:w-1/4 p-2">
                      <div className="border rounded-lg p-4 bg-white shadow-md">
                        <h5 className="text-xl font-bold">20 Mbps</h5>
                        <p>Fast web browsing</p>
                        <p>SD Movie & music streaming</p>
                        <p>HD TV programming</p>
                        <p>Multiple device streaming</p>
                        <p>Superfast video downloads</p>
                        <p>CCTV devices Capability</p>
                        <p className="font-bold">Kshs 5600 for 30 days</p>
                      </div>
                    </div>
                    <div className="w-full md:w-1/4 p-2">
                      <div className="border rounded-lg p-4 bg-white shadow-md">
                        <h5 className="text-xl font-bold">40 Mbps</h5>
                        <p>Fast web browsing</p>
                        <p>UHD Movie & music streaming</p>
                        <p>UHD TV programming</p>
                        <p>Multiple device streaming</p>
                        <p>Superfast video downloads</p>
                        <p>CCTV devices Capability</p>
                        <p className="font-bold">Kshs 8000 for 30 days</p>
                      </div>
                    </div>
                  </div>
                </div>
              </section>
        
              <img src="{% static 'images/itech profile-pages-images-6.jpg' %}" alt="About Us" className="img-fluid rounded" />
              {/* Testimonials Section */}
              <section className="bg-gray-100 py-5">
                <div className="container mx-auto">
                  <h2 className="text-center text-2xl font-bold mb-5">Customer Testimonials</h2>
                  <div className="flex flex-wrap">
                    <div className="w-full md:w-1/2 p-2">
                      <div className="border rounded-lg p-4 bg-white shadow-md">
                        <blockquote className="italic">
                          <p>"Itech Management System has provided us with reliable and fast internet service. We highly recommend them!"</p>
                          <footer className="mt-4">John Doe, CEO at XYZ Corp</footer>
                        </blockquote>
                      </div>
                    </div>
                    <div className="w-full md:w-1/2 p-2">
                      <div className="border rounded-lg p-4 bg-white shadow-md">
                        <blockquote className="italic">
                          <p>"The 24/7 support team is amazing! They are always there to help us with any issues we encounter."</p>
                          <footer className="mt-4">Jane Smith, IT Manager at ABC Inc</footer>
                        </blockquote>
                      </div>
                    </div>
                  </div>
                </div>
              </section>
        
              <img src={itechProfileImage9} alt="Itech Profile Image" className="img-fluid rounded"/>
              {/*  Call-to-Action Section */}
              <section className="bg-primary py-5 text-center">
                <div className="container mx-auto">
                  <h2 className="text-white text-2xl font-bold">Join Us Today</h2>
                  <p className="text-white text-lg">Sign up for our internet plans and experience the best service in town.</p>
                  <Link to="/customer_signup" className="btn bg-white text-primary font-bold py-2 px-4 rounded mt-3">
      Sign Up
    </Link>
                </div>
              </section>
            </div>
            } />
          </Routes>
        </main>

        {/* Footer */}
        <footer className="bg-gray-800 text-white py-4">
          <div className="container mx-auto text-center">
            &copy; {new Date().getFullYear()} Itech Reliable. All rights reserved.
          </div>
        </footer>
      </div>
    </Router>
  );
}

export default App;