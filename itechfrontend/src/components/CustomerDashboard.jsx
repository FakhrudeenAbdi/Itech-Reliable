import React, { useState, useEffect } from 'react';

const CustomerDashboard = () => {
  const [customerData, setCustomerData] = useState(null);

  useEffect(() => {
    const fetchCustomerData = async () => {
      try {
        const response = await fetch('/http://127.0.0.1:8000/api/customer-data/');
        const data = await response.json();
        setCustomerData(data);
      } catch (error) {
        console.error('Error fetching customer data:', error);
      }
    };

    fetchCustomerData();
  }, []);

  if (!customerData) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <h1>Customer Dashboard</h1>
      <h2>Usage History</h2>
      <ul>
        {customerData.usage.map((usage) => (
          <li key={usage.id}>
            {usage.date} - {usage.usage} {usage.unit}
          </li>
        ))}
      </ul>
      <h2>Billing History</h2>
      <ul>
        {customerData.billing.map((bill) => (
          <li key={bill.id}>
            {bill.date} - {bill.amount}
          </li>
        ))}
      </ul>
      <h2>Tickets</h2>
      <ul>
        {customerData.tickets.map((ticket) => (
          <li key={ticket.id}>
            {ticket.description} - {ticket.created_at}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default CustomerDashboard;