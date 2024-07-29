import React from 'react';

function PlanDetail({ plan }) {
  return (
    <div className="container mx-auto mt-10">
      <h1 className="text-3xl font-bold">{plan.name}</h1>
      <p className="text-lg">{plan.description}</p>
      <p className="text-2xl font-bold text-primary">Kshs {plan.price}</p>
    </div>
  );
}

export default PlanDetail;