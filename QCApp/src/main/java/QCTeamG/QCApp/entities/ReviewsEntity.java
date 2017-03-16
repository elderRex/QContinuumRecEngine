package QCTeamG.QCApp.entities;

import java.sql.Date;

import javax.persistence.CascadeType;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.ManyToOne;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Table;


@Entity
@Table(name="reviews")
public class ReviewsEntity {
	
	@Id
    @Column(name="ID")
    @GeneratedValue(strategy=GenerationType.AUTO)
    private Integer id;
	
	@ManyToOne(cascade = CascadeType.ALL)
	@JoinColumn(name="uid",referencedColumnName="id")
    private UsersEntity uid;
     
    @Column(name="Rating")
    private String rating;
    
    @Column(name="Comment")
    private String comment;
    
    @ManyToOne(cascade = CascadeType.ALL)
	@JoinColumn(name="iid",referencedColumnName="id")
    private ItemsEntity iid;
 
    @Column(name="DATETIME")
    public Date date;
     
    public UsersEntity getUid() {
        return uid;
    }
    
    public void setUid(UsersEntity name) {
        this.uid = uid;
    }
    
    public String getRating() {
        return rating;
    }
        
    public void setRating(String rating) {
        this.rating = rating;
    }
    
	public String getComment() {
	  return comment;
	}
	  
	public void setComment(String comment) {
	  this.comment = comment;
	}   

    public Date getDate() {
        return date;
    }

    public void setDate(Date date) {
        this.date = date;
    }
   
    public Integer getId() {
        return id;
    }
    public void setId(Integer id) {
        this.id = id;
    }
    
    public ItemsEntity getIId() {
        return iid;
    }
    public void setIId(ItemsEntity iid) {
        this.iid = iid;
    }
    
}
