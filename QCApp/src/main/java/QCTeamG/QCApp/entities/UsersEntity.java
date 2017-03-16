package QCTeamG.QCApp.entities;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.Id;

import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Table;


@Entity
@Table(name="users")
public class UsersEntity {
	
	@Id
    @Column(name="ID")
    @GeneratedValue(strategy=GenerationType.AUTO)
    private Integer id;
     
    @Column(name="FIRSTNAME")
    private String firstname;
    
    @Column(name="LASTNAME")
    private String lastname;
    
    @Column(name="ENABLED")
    private boolean enabled;
 
    @Column(name="EMAIL")
    public String email;
    
//    @Column(name="username")
//    private String username;
    
    @Column(name="PASSWORD")
    private String password;
     
    public String getEmail() {
        return email;
    }
    
    public void setEmail(String email) {
        this.email = email;
    }
    
//    public String getUserName() {
//        return username;
//    }
//        
//    public void setUserName(String un) {
//        this.username = un;
//    }
    
	public String getPassword() {
	  return password;
	}
	  
	public void setPassword(String password) {
	  this.password = password;
	}   

    public String getFirstname() {
        return firstname;
    }
    public String getLastname() {
        return lastname;
    }
    public void setFirstname(String firstname) {
        this.firstname = firstname;
    }
    public void setLastname(String lastname) {
        this.lastname = lastname;
    }
    public Integer getId() {
        return id;
    }
    public void setId(Integer id) {
        this.id = id;
    }
    
    public void setEnabled(Boolean enabled) {
        this.enabled = enabled;
    }
    
    public boolean getEnabled() {
        return this.enabled;
    }
}
