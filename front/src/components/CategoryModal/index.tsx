import React, { ChangeEvent, useState } from 'react';
import Modal from './../Modal';

interface CategoryModalProps {
  isOpen: boolean;
  onClose: () => void;
  onSubmit: (newCategoryName: string) => void;
}

const CategoryModal: React.FC<CategoryModalProps> = ({
  isOpen,
  onClose,
  onSubmit,
}) => {
  const [newCategoryName, setNewCategoryName] = useState('');

  const handleInputChange = (e: ChangeEvent<HTMLInputElement>) => {
    setNewCategoryName(e.target.value);
  };

  const handleSubmit = () => {
    onSubmit(newCategoryName);
    setNewCategoryName('');
    onClose();
  };

  return (
    <Modal isOpen={isOpen} onClose={onClose}>
      <div>
        <label htmlFor="categoryInput">Введите название категории:</label>
        <input
          type="text"
          id="categoryInput"
          value={newCategoryName}
          onChange={handleInputChange}
        />
        <button onClick={handleSubmit}>Добавить</button>
      </div>
    </Modal>
  );
};

export default CategoryModal;
