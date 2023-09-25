"use client";
import React, { useState } from 'react';
import styles from './navbar.module.css';

function Navbar() {
    const [selectedItem, setSelectedItem] = useState('Inicio');

    const handleItemClick = (item, id) => {
        setSelectedItem(item);
        scrollToSection(id);

    };
   
    const scrollToSection = (id) => {
        const section = document.getElementById(id);
        if (section) {
            section.scrollIntoView({ behavior: 'smooth'})

        }

    };

    return (
        <nav className={styles.navbar}>
            <div 
                className={styles.navbarItem + ` ${selectedItem === 'Inicio' ? styles.selected : ''}`}
                onClick={() => handleItemClick('Inicio', 'header')}
            >
                <a href="#header">Inicio</a>
            </div>
            <div 
                className={styles.navbarItem + ` ${selectedItem === 'Skills' ? styles.selected : ''}`}
                onClick={() => handleItemClick('Skills', 'info')}
            >
                <a href="#info">Skills</a>
            </div>
        </nav>
    );

}

export default Navbar;