package com.javastudy;

import java.util.ArrayList;
import java.util.NoSuchElementException;

/**
 * This is a class that holds a list of Contact.
 * Its main purpose is to abstract the list of Contacts implementation.
 * */
public class Contacts {
    private ArrayList<Contact> contacts = new ArrayList<>();

    public ArrayList<Contact> getContacts() {
        return contacts;
    }

    public void setContacts(ArrayList<Contact> contacts) {
        this.contacts = contacts;
    }

    public void addNewContact(Contact contact){
        // check if the contact name is already installed
        try {
            findByNameReturnIndex(contact.getName());
            System.out.println("store: Sorry, that name is already being used by a contact in the list.");
        } catch (NoSuchElementException e) {
            // if the code goes through here it means that no contact with that name was found
            this.contacts.add(contact);
            System.out.println("store: Contact saved successfully.");
        }
    }

    public int getContactsLength(){
        return this.contacts.size();
    }

    public Contact getContactByIndex(int index){
        return this.contacts.get(index);
    }

    public void removeContact(String name){

    }

    // build function findByNameReturnIndex, which is private
    // return the index of the contact in the ArrayList
    private int findByNameReturnIndex(String contactName) {
        for (int i = 0; i < this.contacts.size(); i++) {
            Contact contact = contacts.get(i);
            if (contactName == contact.getName()) {
                return i;
            }
        }
        // in here we experiment by throwing an error
        // we could do this by sending null
        throw new NoSuchElementException("Contact not found.");
    }
}
