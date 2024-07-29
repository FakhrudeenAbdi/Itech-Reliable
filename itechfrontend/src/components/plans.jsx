import React from 'react';

function Plans() {
  const plans = [
    {
      id: 1,
      name: '8 Mbps',
      description: [
        'Fast web browsing',
        'SD Movie & music streaming',
        'SD TV programming',
        'CCTV devices Capability',
        'Multiple device streaming',
        'Superfast video downloads',
      ],
      price: 2500,
    },
    {
      id: 2,
      name: '10 Mbps',
      description: [
        'HD streaming',
        'YouTube streaming',
        'CCTV cameras',
        'Movie download',
        'Online video streaming',
        'Multiple device streaming',
      ],
      price: 3500,
    },
    {
      id: 3,
      name: '20 Mbps',
      description: [
        'Fast web browsing',
        'SD Movie & music streaming',
        'HD TV programming',
        'Multiple device streaming',
        'Superfast video downloads',
        'CCTV devices Capability',
      ],
      price: 5600,
    },
    {
      id: 4,
      name: '40 Mbps',
      description: [
        'Fast web browsing',
        'UHD Movie & music streaming',
        'UHD TV programming',
        'Multiple device streaming',
        'Superfast video downloads',
        'CCTV devices Capability',
      ],
      price: 8000,
    },
  ];

  return (
    <div className="container mx-auto my-10">
      <h1 className="text-3xl font-bold mb-5">Our Plans</h1>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        {plans.map((plan) => (
          <div key={plan.id} className="bg-white rounded-lg shadow-md">
            <div className="p-4">
              <h5 className="text-xl font-bold">{plan.name}</h5>
              {plan.description.map((feature, index) => (
                <p key={index} className="text-gray-600">
                  {feature}
                </p>
              ))}
              <p className="text-2xl font-bold text-primary">Kshs {plan.price}</p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Plans;