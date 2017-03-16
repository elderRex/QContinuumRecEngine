package QCTeamG.QCApp.entities;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import javax.persistence.Table;

@Entity
@Table(name="user_roles")
public class UserRolesEntity {
     
	@Id
    @Column(name="id")
    @GeneratedValue
    private Integer id;
     
    @Column(name="EMAIL")
    private String email;
    
    @Column(name="ROLE")
    private String role;
    
    public String getEmail() {
        return email;
    }
    
    public void setEmail(String email) {
        this.email = email;
    }
    
    public String getRole() {
        return role;
    }
    
    public void setRole(String role) {
        this.role = role;
    }
    
    public Integer getId() {
        return id;
    }
    
        
}