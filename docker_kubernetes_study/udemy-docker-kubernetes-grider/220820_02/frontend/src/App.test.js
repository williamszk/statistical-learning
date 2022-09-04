import { render, screen } from '@testing-library/react';
import App from './App';

test('renders learn react link', () => {
  console.log("Monkey! Running test 1");
  render(<App />);
  const linkElement = screen.getByText(/learn react/i);
  expect(linkElement).toBeInTheDocument();
});


test('renders learn react link', () => {
  console.log("Monkey! Running test 2");
  render(<App />);
  const linkElement = screen.getByText(/learn react/i);
  expect(linkElement).toBeInTheDocument();
});

