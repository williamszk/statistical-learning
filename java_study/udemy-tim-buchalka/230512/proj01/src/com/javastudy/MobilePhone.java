package com.javastudy;

import java.util.NoSuchElementException;

public class MobilePhone {
    private Contacts contacts = new Contacts();

    public void store(Contact contact) {
    }

    public void modify(String name, Contact contact) {
        // find the index of the contact and replace it
        int idx = 0;
        try {
            idx = findByNameReturnIndex(name);
        } catch (NoSuchElementException e) {
            System.out.println("modify: Sorry, we couldn't find a contact with the specified name.");
            return;
        }
        this.contacts.set(idx, contact);
        System.out.println("modify: Contact changed successfully.");
    }

    public void remove(String contactName) {
        Contact contact = null;
        try {
            int idx = findByNameReturnIndex(contactName);
            this.contacts.remove(idx);
        } catch (NoSuchElementException e) {
            System.out.println("Sorry, we couldn't find the name of this contact.");
        }
    }

    public Contact query(String contactName) {
        Contact contact = null;
        try {
            int idx = findByNameReturnIndex(contactName);
            contact = this.contacts.get(idx);
        } catch (NoSuchElementException e) {
            System.out.println("Sorry, the contact that you are looking for doesn't exist.");
        }

        // we have two options to pass information in case of failure:
        // 1. throw an error
        // 2. send nulls
        //
        // the second option is more like railway error handling
        // we pass the information that something is wrong by sending a null value
        // using comma err, comma ok, or Result (Rust enum) can carry more information
        // using throw and try-catch can make the code verbose, but I'd like to to use it to see
        // what happens

        // in here we experiment by sending a null
        // we could do this by throwing an error...
        return contact;
    }

}
