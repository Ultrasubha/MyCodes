import { Fragment } from "react/jsx-runtime";
import { MouseEvent, useState } from "react";

interface Props {
  Delicacies: string[];
  heading: string;
  onSelectItem: (food: String) => void;
}

function ListGroup({ Delicacies, heading, onSelectItem }: Props) {
  // Event Handler
  const handleClick = (event: MouseEvent) => console.log(event);
  const [selectedFood, setSelectedFood] = useState(-1);

  return (
    <Fragment>
      <h1>{heading}</h1>
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
            onClick={() => {
              setSelectedFood(foodIndex);
              onSelectItem(food);
            }}
          >
            {food}
          </li>
        ))}
      </ul>
    </Fragment>
  );
}

export default ListGroup;
