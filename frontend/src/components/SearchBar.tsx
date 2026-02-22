import { useState } from "react"

interface Props {
  onSearch: (query: string) => void
  
}

export default function SearchBar({ onSearch }: Props) {
  const [query, setQuery] = useState("")

  const handleSubmit: React.FormEventHandler<HTMLFormElement> = (e) => {
    e.preventDefault();
    console.log("SUBMIT fired", query);
    onSearch(query);
  };

  return (

    <form onSubmit={handleSubmit}>
      <input
        type="text"
        placeholder="Search for a movie..."
        value={query}
        onChange={(e) => setQuery(e.target.value)}
      />
      <button type="submit">Search</button>
    </form>
  )
}
