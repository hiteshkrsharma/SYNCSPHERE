import { Button } from "@/components/ui/button";
export default function Home() {
  return (
    <div>
      <Button className="flex gap-4">
        primary
      </Button>
      <Button variant="secondary">
        secondary
      </Button>
      <Button variant="destructive">
        Destructive
      </Button>
      <Button variant="ghost">
        Ghost
      </Button>
      <Button variant="link">
        Link
      </Button>
      <Button variant="outline">
        Outline      
      </Button>
    </div>
  );
}