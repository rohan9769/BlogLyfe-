import './App.css';
import {BrowserRouter as Router,Route,Switch} from 'react-router-dom'
import Layout from './components/Layout'
import Home from './components/Home'
import Blog from './components/Blog'
import BlogDetail from './components/BlogDetail'
import Category from './components/Category'


function App() {
  return (
    <>
      <Router>
        <Layout>
          <Switch>
            <Route exact path='/' component={Home}></Route>
            <Route exact path='/blog' component={Blog}></Route>
            <Route exact path='/category/:id' component={Category}></Route>
            <Route exact path='/blog/:id' component={BlogDetail}></Route>
          </Switch>
        </Layout>
      </Router>
    </>
  );
}

export default App;
