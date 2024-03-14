const getUser = (userId) => {
    return new Promise((resolve, reject) => {
      // Simulating an asynchronous operation
      setTimeout(() => {
        const user = {
          id: userId,
          username: "john_doe",
        };
        resolve(user);
      }, 1000);
    });
  };
  
  const getUserPosts = (user) => {
    return new Promise((resolve, reject) => {
      // Simulating another asynchronous operation
      setTimeout(() => {
        const posts = [
          { id: 1, title: "Post 1" },
          { id: 2, title: "Post 2" },
        ];
        resolve({ user, posts });
      }, 1000);
    });
  };
  
  const displayUserPosts = (data) => {
    console.log("User:", data.user);
    console.log("Posts:", data.posts.map(post => post.title).join(", "));
  };
  
  // Using promise chaining to avoid callback hell
  getUser(123)
    .then((user) => getUserPosts(user))
    .then((userData) => displayUserPosts(userData))
    .catch((error) => console.error(error.message));
  