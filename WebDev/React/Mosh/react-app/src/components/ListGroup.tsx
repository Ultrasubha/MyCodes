import { Fragment } from "react/jsx-runtime";
import { MouseEvent, useState } from "react";
function ListGroup() {
  const Delicacies = [
    "Biriyani",
    "Mutton Curry",
    "Prawn Malaicurry",
    "KFC",
    "Mustard Hilsha",
  ];

  // Event Handler
  const handleClick = (event: MouseEvent) => console.log(event);
  const [selectedFood, setSelectedFood] = useState(-1);

  return (
    <Fragment>
      <h1>Delicacies</h1>
      {Delicacies.length < 1 && <p> No items found</p>}
      <ul className="list-group">
        {Delicacies.map((food, foodIndex) => (
          <li
            className={
              selectedFood === foodIndex
                ? "list-group-item active"
                : "list-group-item"
            }
            key={food}
            onClick={()=>setSelectedFood(foodIndex)}
          >
            {food}
          </li>
        ))}
      </ul>
    </Fragment>
  );
}

export default ListGroup;
