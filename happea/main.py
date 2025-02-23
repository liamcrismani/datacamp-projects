from typing import Optional, List, Any


class Wedding:
    """Wedding event class."""
   
    def __init__(self, bride_name: str, groom_name: str):
        self.bride_name = bride_name
        self.groom_name = groom_name
        self.confirmed_guest_list: List[Guest] = list()
        self.invitation_list: List[Invitation] = list()


    def send_invitation(self, name:str, email: str, is_special: bool = False) -> None:
        if email in self.invitation_list:
            print(f"Guest with email {email} already exists")
        if is_special:
            new_guest = SpecialGuest(name, email, self)
        else:
            new_guest = Guest(name, email, self)
        self.invitation_list.append(Invitation(guest=new_guest))


    def retrieve_invitation(self, email: str) -> Optional['Invitation']:
        # Method to retrieve an invitation using the guest's email address.
        # Parameters:
        # - email: The email address of the guest.
        # Returns: The Invitation object if found, otherwise None.
        for invitation in self.invitation_list:  # Iterate through all invitations.
            if invitation.guest.email == email:  # Check if the email matches.
                return invitation  # Return the matching invitation.
        return None  # Return None if no matching invitation is found.
    

    def get_guest_by_email(self, email: str) -> Any:
       """"Return matching guest from searched email."""
       for invitation in self.invitation_list:
           if invitation.guest.email == email:
               return invitation.guest
           else:
               return None


class Invitation:
    """Representation of wedding invitation."""

    def __init__(self, guest: Guest):
        self.guest = guest
        self.status: str = "pending"

    def accept(self):
        """Update invitation status to 'accepted'."""
        self.status = "accepted"

    def decline(self):
        """Update invitation status to 'declined'."""
        self.status = "accepted"


class Guest:
    #Complete the implementation of the Guest Class here 
    def __init__(self, name: str, email: str, wedding: Wedding, inviting_guest_email: Optional[str] = None) -> None:
        # The __init__ method initializes a new instance of the Guest class.
        # Parameters:
        # - name: The name of the guest.
        # - email: The email address of the guest.
        # - wedding: The Wedding object to which the guest is invited.
        # - inviting_guest_email: The email address of the guest who invited this guest (for plus-ones, default is None).
        self.name: str = name  # Instance variable to store the guest's name.
        self.email: str = email  # Instance variable to store the guest's email address.
        self.wedding: Wedding = wedding  # Instance variable to store the associated Wedding object.
        self.inviting_guest_email: Optional[str] = inviting_guest_email  # Email of the guest who invited this guest, if any.

    def accept_invitation(self) -> None:
        # Method for the guest to accept their invitation.
        invitation = self.wedding.retrieve_invitation(self.email)  # Retrieve the guest's invitation.
        if invitation:  # Check if an invitation exists.
            invitation.accept()  # Mark the invitation as accepted.
            if self not in self.wedding.confirmed_guest_list:  # If the guest is not already confirmed:
                self.wedding.confirmed_guest_list.append(self)  # Add the guest to the confirmed guest list.


    def decline_invitation(self) -> None:
        """Decline invitation."""
        invitation = self.wedding.retrieve_invitation(self.email)
        if invitation:
            invitation.decline()
            if self in self.wedding.confirmed_guest_list:
                self.wedding.confirmed_guest_list.remove(self)


class SpecialGuest(Guest):
    #Complete the implementation of the SpecialGuest Class here    
    def __init__(self, name: str, email: str, wedding: Wedding, 
                 inviting_guest_email: Optional[str] = None, plus_one: Optional[str] = None):
        super().__init__(name, email, wedding, inviting_guest_email)
        self.plus_one = plus_one
        
    
    def invite_plus_one(self, name: str, email: str):
        """Extend an Invitation to another Guest."""
        if self.plus_one:
            print(f"Already invited a plus one")
            return 
        if email not in self.wedding.confirmed_guest_list:
            self.wedding.send_invitation(name, email)
            self.plus_one = self.wedding.get_guest_by_email(email)
            print(f"Plus one invitation sent to {email}")
        

    def uninvite_plus_one(self) -> None:
        # Method to uninvite the special guest's plus-one.
        # Parameters:
        # - self: The SpecialGuest instance.
        if self.plus_one:  # Check if a plus-one exists.
            invitation = self.wedding.retrieve_invitation(self.plus_one.email)  # Retrieve plus-one's invitation.
            self.wedding.invitation_list.remove(invitation)  # Remove invitation from wedding list.

            if self.plus_one in self.wedding.confirmed_guest_list:  # If plus-one is in confirmed list.
                self.wedding.confirmed_guest_list.remove(self.plus_one)  # Remove plus-one from confirmed list.

            self.plus_one = None  # Reset plus-one reference to None.
