package whu.ybg.springboot06jpa.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import whu.ybg.springboot06jpa.User;

public interface UserRepository extends JpaRepository<User, Integer> {
}
